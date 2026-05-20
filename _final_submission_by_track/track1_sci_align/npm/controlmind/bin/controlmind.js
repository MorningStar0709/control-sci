#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const args = process.argv.slice(2);
const isWindows = process.platform === "win32";

function exists(filePath) {
  try {
    return fs.existsSync(filePath);
  } catch {
    return false;
  }
}

function isProjectRoot(dir) {
  return exists(path.join(dir, "controlsci")) && exists(path.join(dir, "pyproject.toml"));
}

function findUp(startDir) {
  let current = path.resolve(startDir);
  while (true) {
    if (isProjectRoot(current)) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return null;
    }
    current = parent;
  }
}

function findProjectRoot() {
  const candidates = [
    process.env.CONTROLMIND_HOME,
    process.cwd(),
    path.resolve(__dirname, "..", "..", ".."),
  ].filter(Boolean);

  for (const candidate of candidates) {
    const direct = path.resolve(candidate);
    if (isProjectRoot(direct)) {
      return direct;
    }
    const upward = findUp(direct);
    if (upward) {
      return upward;
    }
  }
  return null;
}

function run(command, commandArgs) {
  return spawnSync(command, commandArgs, {
    env: process.env,
    stdio: "pipe",
    encoding: "utf8",
    shell: false,
  });
}

function commandWorks(command, commandArgs) {
  const result = run(command, commandArgs);
  return !result.error && result.status === 0;
}

function findPythonLauncher() {
  if (process.env.CONTROLMIND_PYTHON) {
    return { command: process.env.CONTROLMIND_PYTHON, argsPrefix: [], label: "CONTROLMIND_PYTHON" };
  }

  if (commandWorks("conda", ["run", "-n", "myenv", "python", "--version"])) {
    return { command: "conda", argsPrefix: ["run", "--no-capture-output", "-n", "myenv", "python"], label: "conda:myenv" };
  }

  const pythonCommands = isWindows ? ["python", "py"] : ["python3", "python"];
  for (const command of pythonCommands) {
    if (commandWorks(command, ["--version"])) {
      return { command, argsPrefix: [], label: command };
    }
  }
  return null;
}

function printWrapperDoctor(projectRoot, pythonLauncher) {
  console.log("ControlMind npm launcher");
  console.log(`  project: ${projectRoot || "not found"}`);
  console.log(`  python:  ${pythonLauncher ? pythonLauncher.label : "not found"}`);
  console.log("");
  console.log("Resolution order:");
  console.log("  1. CONTROLMIND_HOME");
  console.log("  2. current working directory and parent directories");
  console.log("  3. repository root relative to this npm package");
  console.log("");
  console.log("Python order:");
  console.log("  1. CONTROLMIND_PYTHON");
  console.log("  2. conda run -n myenv python");
  console.log("  3. python3/python on PATH");
}

function fail(message, details = []) {
  console.error(`ControlMind launcher error: ${message}`);
  for (const detail of details) {
    console.error(`  - ${detail}`);
  }
  process.exit(1);
}

const projectRoot = findProjectRoot();
const pythonLauncher = findPythonLauncher();

if (args[0] === "wrapper-doctor") {
  printWrapperDoctor(projectRoot, pythonLauncher);
  process.exit(projectRoot && pythonLauncher ? 0 : 1);
}

if (!projectRoot) {
  fail("could not locate the ControlMind project root.", [
    "Run this command inside the repository, or set CONTROLMIND_HOME to the repository path.",
  ]);
}

if (!pythonLauncher) {
  fail("could not find a usable Python runtime.", [
    "Install Python 3.10+, activate your environment, or set CONTROLMIND_PYTHON.",
    "For this workspace, the recommended runtime is the myenv Conda environment.",
  ]);
}

const pythonArgs = [...pythonLauncher.argsPrefix, "-m", "controlsci.cli", ...args];
const result = spawnSync(pythonLauncher.command, pythonArgs, {
  cwd: projectRoot,
  env: {
    ...process.env,
    PYTHONPATH: [projectRoot, process.env.PYTHONPATH].filter(Boolean).join(path.delimiter),
  },
  stdio: "inherit",
  shell: false,
});

if (result.error) {
  fail(`failed to start ${pythonLauncher.label}.`, [result.error.message]);
}

process.exit(result.status ?? 1);
