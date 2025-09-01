// Simple copy-to-clipboard for the <code> block
document.getElementById('copy').addEventListener('click', function(){
  const code = document.getElementById('snippet').innerText;
  navigator.clipboard.writeText(code).then(() => {
    const btn = document.getElementById('copy');
    const prev = btn.textContent;
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = prev, 1200);
  });
});
