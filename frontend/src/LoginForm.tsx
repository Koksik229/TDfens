import React, { useState } from 'react';

const API_BASE = 'http://localhost:8000/auth';

function LoginForm() {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [result, setResult] = useState('');

  const validate = () => {
    const errors = [];
    if (login.trim().length < 3) {
      errors.push('Логин должен быть от 3 символов');
    }
    if (password.trim().length < 6) {
      errors.push('Пароль должен быть от 6 символов');
    }
    return errors;
  };

  const handleSubmit = async (url: string) => {
    const localErrors = validate();
    if (localErrors.length > 0) {
      setResult('❌ Ошибка:\n' + localErrors.map(e => '• ' + e).join('\n'));
      return;
    }

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ login, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem('token', data.access_token);
        window.location.href = '/map';
      } else {
        if (Array.isArray(data.detail)) {
          const messages = data.detail.map((e: any) => `• ${e.msg}`).join('\n');
          setResult('❌ Ошибка:\n' + messages);
        } else if (typeof data.detail === 'string') {
          setResult('❌ Ошибка: ' + data.detail);
        } else {
          setResult('❌ Неизвестная ошибка: ' + JSON.stringify(data));
        }
      }
    } catch (error) {
      setResult('❌ Ошибка при соединении: ' + String(error));
    }
  };

  return (
    <div className="form-container">
      <h1>Tower Defence</h1>
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
      <pre className="result">{result}</pre>
    </div>
  );
}

export default LoginForm;
