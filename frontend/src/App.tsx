import React from 'react';
import LoginForm from './LoginForm';
<<<<<<< HEAD
import MapScreen from './MapScreen';

function App() {
  const path = window.location.pathname;

  if (path === '/map') {
    return <MapScreen />;
  }

  return <LoginForm />;
=======

function App() {
  return (
    <div className="app">
      <h1>Tower Defence</h1>
      <LoginForm />
    </div>
  );
>>>>>>> 71d4628bb2d5f6ecfeb6110ebe4b36fce3dbf7f2
}

export default App;
