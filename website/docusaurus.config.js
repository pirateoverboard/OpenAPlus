// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'OpenAPlus',
  tagline: 'Open learning for CompTIA certifications',
  favicon: 'img/favicon.svg',
  url: 'https://openaplus.github.io',
  baseUrl: '/OpenAPlus/',
  organizationName: 'OpenAPlus',
  projectName: 'OpenAPlus',
  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },
  trailingSlash: false,
  presets: [
    [
      'classic',
      {
        // Enable docs when the first original educational content is ready.
        docs: false,
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'OpenAPlus',
      items: [
        {
          href: 'https://github.com/OpenAPlus/OpenAPlus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright:
        `Copyright © ${new Date().getFullYear()} OpenAPlus contributors. ` +
        'Code: MIT. Educational content: CC BY 4.0.',
    },
  },
};

module.exports = config;
