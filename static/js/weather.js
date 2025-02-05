document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weatherForm');
    const infoDiv = document.querySelector('.info');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const city = document.getElementById('cityInput').value;
        
        try {
            // First, get coordinates
            const geoUrl = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(city)}&format=json`;
            const geoResponse = await fetch(geoUrl);
            const geoData = await geoResponse.json();

            if (!geoData.length) {
                throw new Error('City not found');
            }

            const { lat, lon } = geoData[0];

            // Get weather data from NWS API
            const pointsResponse = await fetch(`https://api.weather.gov/points/${lat},${lon}`);
            if (!pointsResponse.ok) {
                throw new Error('Weather service error');
            }
            const pointsData = await pointsResponse.json();

            // Get forecast
            const forecastResponse = await fetch(pointsData.properties.forecast);
            if (!forecastResponse.ok) {
                throw new Error('Forecast error');
            }
            const forecastData = await forecastResponse.json();
            const currentPeriod = forecastData.properties.periods[0];

            // Update the display
            infoDiv.innerHTML = `
                <p>Location: ${city}</p>
                <p>Weather Condition: ${currentPeriod.shortForecast}</p>
                <p>Temperature: ${currentPeriod.temperature}°${currentPeriod.temperatureUnit}</p>
                <img src="${currentPeriod.icon}" alt="Weather conditions">
            `;

        } catch (error) {
            infoDiv.innerHTML = `<p>Error: ${error.message}. Please try a different US city.</p>`;
            console.error('Weather fetch error:', error);
        }
    });
});
