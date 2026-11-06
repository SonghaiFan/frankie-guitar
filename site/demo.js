// A small recorded-UI explorer, not a reimplementation of the chord engine.
const controls = [...document.querySelectorAll('[data-shape]')];
const image = document.querySelector('#shape-image');
const link = document.querySelector('#shape-link');
const status = document.querySelector('#shape-status');
controls.forEach(button => button.addEventListener('click', () => {
  controls.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  image.src = image.src.replace(/caged-[caged]\.png$/, `caged-${button.dataset.shape}.png`);
  link.href = image.src;
  status.textContent = `${button.dataset.shape.toUpperCase()} ${button.querySelector('span').textContent} · ${button.dataset.frets}`;
}));
