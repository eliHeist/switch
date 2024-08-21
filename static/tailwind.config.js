module.exports = {
    content: ['../templates/*.html', '../**/templates/**/*.html'],
    darkMode: 'media', // or 'class'
    theme: {
      extend: {
        colors: {
          'primary': 'rgb(89, 31, 96)',
          'secondary': 'rgb(153, 66, 111)',
          'accent': 'rgb(0, 194, 255)',
          'danger': 'rgb(227, 17, 17)',
          'success': 'rgb(0, 136, 68)',
          'warning': 'rgb(255, 153, 0)',
          'black': 'rgb(32, 29, 33)',
          'white': 'rgb(254, 254, 254)',
          'grey': 'rgb(114, 103, 115)',
          'light': 'rgb(222, 205, 223)',
        },
      },
    },
    variants: {
      extend: {},
    },
    plugins: [],
    darkMode: 'media',
  };
  