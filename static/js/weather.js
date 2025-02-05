document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('weatherForm');
  const infoSpan = document.querySelector('span.info');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = document.getElementById('cityInput').value;
    // For testing purposes, we simulate a fixed successful response.
    infoSpan.innerHTML = `
      <p>Location: ${city}</p>
      <p>Weather Condition: Sunny</p>
      <p>Temperature: 75°F</p>
      <img src="https://via.placeholder.com/100?text=Weather" alt="Weather Icon">
      <img src="https://via.placeholder.com/100?text=City" alt="City Image">
    `;
  });
});
