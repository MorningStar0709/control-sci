import Head from 'next/head';
import '../styles/globals.css';
import 'katex/dist/katex.min.css';
import { AnimatePresence, LazyMotion, domAnimation } from 'framer-motion';
import TopStatusBar from '../components/workbench/TopStatusBar';
import Sidebar from '../components/workbench/Sidebar';
import { RuntimeProvider, useRuntime } from '../components/workbench/RuntimeProvider';

function WorkbenchApp({ Component, pageProps }) {
  const { runtimeConfig } = useRuntime();
  return (
    <>
      <Head>
        <title>ControlMind 成果展示台</title>
        <meta name="description" content="ControlMind 在线展示版：MinerU 官方 API、DeepSeek、公开/脱敏材料闭环展示。" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.svg?v=controlmind-20260516" type="image/svg+xml" />
      </Head>
      <LazyMotion features={domAnimation}>
        <AnimatePresence>
          <div key="shell" className="flex flex-col min-h-screen">
            <TopStatusBar />
            <div className="flex flex-1">
              <Sidebar />
              <main className="flex-1 overflow-auto">
                <Component {...pageProps} profile={runtimeConfig.profile} runtimeConfig={runtimeConfig} />
              </main>
            </div>
          </div>
        </AnimatePresence>
      </LazyMotion>
    </>
  );
}

export default function App(props) {
  return (
    <RuntimeProvider>
      <WorkbenchApp {...props} />
    </RuntimeProvider>
  );
}
