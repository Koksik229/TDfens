import React, { useState } from 'react';

const API_BASE = 'http://localhost:8000/auth';

function LoginForm() {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (url: string) => {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ login, password }),
    });
    const data = await response.json();
    if (response.ok) {
      setResult('✅ Успешно! Токен: ' + data.access_token);
    } else {
      setResult('❌ Ошибка: ' + (data.detail || 'неизвестно'));
    }
  };

  return (
    <div className="form-container">
      <input
        type="text"
        placeholder="Логин"
        value={login}
        onChange={(e) => setLogin(e.target.value)}
      />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <div className="buttons">
        <button onClick={() => handleSubmit(API_BASE + '/register')}>Зарегистрироваться</button>
        <button onClick={() => handleSubmit(API_BASE + '/login')}>Войти</button>
      </div>
      <div className="result">{result}</div>
    </div>
  );
}

export default LoginForm;
