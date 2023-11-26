import React from 'react'
import { Article } from './Article'

export const Main = () => {
  return (
    <main className='main container'>
      <h1 className='main__title'>Bem-vindo ao TODOApp</h1>
      <p className='main__text'>
        Mantenha anotado as tarefas do seu dia!
      </p>
      <Article />
    </main>
  )
}
