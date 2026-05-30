import { useState } from 'react';
import Head from "next/head";
import "../styles/globals.css";
import "katex/dist/katex.min.css";
import { AnimatePresence, LazyMotion, domAnimation } from "framer-motion";
import TopStatusBar from "../components/workbench/TopStatusBar";
import Sidebar from "../components/workbench/Sidebar";
import SettingsDrawer from "../components/workbench/SettingsDrawer";
import { AskSessionProvider } from "../components/workbench/AskSessionProvider";
import { RuntimeProvider, useRuntime } from "../components/workbench/RuntimeProvider";
import { applyProfilePreset } from "../lib/runtimeDefaults";

function WorkbenchApp({ Component, pageProps }) {
  const [drawerOpen, setDrawerOpen] = useState(false);
  const { runtimeConfig, setRuntimeConfig } = useRuntime();

  return (
    <>
      <Head>
        <title>ControlMind 科学复现工作台</title>
        <meta name='description' content='本地优先的科学复现工作台：解析、评测、Agent 和 Medical RAG 一体化验证。' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.svg?v=controlmind-20260516' type='image/svg+xml' />
      </Head>
      <LazyMotion features={domAnimation}>
        <AnimatePresence>
          <div key="shell" className="flex flex-col min-h-screen">
            <TopStatusBar profile={runtimeConfig.profile} onProfileChange={(p) => setRuntimeConfig(applyProfilePreset(runtimeConfig, p))} onOpenSettings={() => setDrawerOpen(true)} />
            <div className="flex flex-1">
              <Sidebar />
              <main className="flex-1 overflow-auto">
                <Component {...pageProps} profile={runtimeConfig.profile} runtimeConfig={runtimeConfig} />
              </main>
            </div>
          </div>
          <SettingsDrawer key="drawer" open={drawerOpen} onClose={() => setDrawerOpen(false)} runtimeConfig={runtimeConfig} onConfigChange={setRuntimeConfig} />
        </AnimatePresence>
      </LazyMotion>
    </>
  );
}

export default function App(props) {
  return (
    <RuntimeProvider>
      <AskSessionProvider>
        <WorkbenchApp {...props} />
      </AskSessionProvider>
    </RuntimeProvider>
  );
}
