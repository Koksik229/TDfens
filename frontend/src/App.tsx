import React from 'react';
import LoginForm from './LoginForm';
import MapScreen from './MapScreen';

function App() {
  const path = window.location.pathname;

  if (path === '/map') {
    return <MapScreen />;
  }

  return <LoginForm />;
}

export default App;
