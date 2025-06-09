import React from 'react';

function MapScreen() {
  const token = localStorage.getItem('token');

  if (!token) {
    window.location.href = '/';
    return null;
  }

  return (
    <div className="map-screen">
      <h2>🗺️ Карта уровней</h2>
      <p>Добро пожаловать! Токен найден ✅</p>
      {/* Здесь потом будет загрузка карты и прогресса */}
    </div>
  );
}

export default MapScreen;
