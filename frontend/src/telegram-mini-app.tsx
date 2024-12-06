'use client'

import React, { useEffect, useState } from 'react'
import { WebApp } from '@twa-dev/sdk'

interface User {
  id: number;
  first_name: string;
  username?: string;
}

declare global {
  interface Window {
    Telegram: {
      WebApp: typeof WebApp;
    }
  }
}

export default function TelegramMiniApp() {
  const [user, setUser] = useState<User | null>(null)
  const [error, setError] = useState<string>('')

  useEffect(() => {
    try {
      const webApp = window.Telegram?.WebApp
      if (webApp) {
        const webAppUser = webApp.initDataUnsafe.user
        if (webAppUser) {
          setUser({
            id: webAppUser.id,
            first_name: webAppUser.first_name,
            username: webAppUser.username
          })
        }
      }
    } catch (err) {
      setError('Failed to get user data')
    }
  }, [])

  if (error) {
    return <div className="p-4 text-red-500">{error}</div>
  }

  if (!user) {
    return <div className="p-4">This app can only be accessed through Telegram.</div>
  }

  return (
    <div className="p-4">
      <h1 className="text-xl mb-4">User Info</h1>
      <div>
        <p>ID: {user.id}</p>
        <p>Name: {user.first_name}</p>
        {user.username && <p>Username: @{user.username}</p>}
      </div>
    </div>
  )
}
