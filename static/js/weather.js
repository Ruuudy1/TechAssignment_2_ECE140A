document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weatherForm');
    const infoSpan = document.querySelector('span.info');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const city = document.getElementById('cityInput').value;
      try {
        // (In a real app, you would perform API calls here.)
        // For testing, simply simulate valid data:
        infoSpan.innerHTML = `
          <p>Location: ${city}</p>
          <p>Weather Condition: Sunny</p>
          <p>Temperature: 75°F</p>
        `;
      } catch (error) {
        infoSpan.innerHTML = `<p>Error fetching weather data</p>`;
      }
    });
  });
  