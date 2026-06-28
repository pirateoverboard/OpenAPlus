import clsx from 'clsx';
import Heading from '@theme/Heading';
import Layout from '@theme/Layout';
import styles from './index.module.css';

export default function Home() {
  return (
    <Layout
      title="Open learning"
      description="An open-source learning platform for CompTIA certifications"
    >
      <main className={clsx('container', styles.main)}>
        <Heading as="h1">OpenAPlus</Heading>
        <p className={styles.subtitle}>
          An open-source learning platform for CompTIA certifications.
        </p>
        <p>The platform is under construction. Educational content is coming later.</p>
        <a
          className="button button--primary button--lg"
          href="https://github.com/OpenAPlus/OpenAPlus"
        >
          View the repository
        </a>
      </main>
    </Layout>
  );
}
