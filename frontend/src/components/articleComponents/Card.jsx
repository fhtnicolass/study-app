import React from 'react';
import moment from 'moment';
import 'moment/locale/pt-br';

import { FiEdit, FiTrash2 } from 'react-icons/fi';

moment.locale('pt-br');

export const Card = ({
  idTask,
  title,
  description,
  timestamp,
  getTask,
  deleteTask,
}) => {
  const momentTimestamp = moment(timestamp);

  const timeAgo = momentTimestamp.fromNow();
  const createdText = momentTimestamp.isBefore(moment(), 'day')
    ? 'Criado em:'
    : 'Criado hoje:';

  // Tradução manual de algumas mensagens do Moment.js
  const translatedTimeAgo = timeAgo
    .replace('a few seconds ago', 'alguns segundos atrás')
    .replace('a minute ago', 'um minuto atrás')
    .replace('minutes ago', 'minutos atrás')
    .replace('an hour ago', 'uma hora atrás')
    .replace('hours ago', 'horas atrás')
    .replace('a day ago', 'um dia atrás')
    .replace('days ago', 'dias atrás')
    .replace('a month ago', 'um mês atrás')
    .replace('months ago', 'meses atrás')
    .replace('a year ago', 'um ano atrás')
    .replace('years ago', 'anos atrás');

  return (
    <div className='cards__card'>
      <h2 className='cards__card-title'>{title}</h2>
      <p className='cards__card-description'>{description}</p>
      <p className='cards__card-timestamp'>
        {createdText} {translatedTimeAgo}
      </p>
      <div className='cards__card-btns'>
        <button
          className='cards__card-btns_edit'
          type='button'
          onClick={() => getTask(idTask)}
        >
          <FiEdit className='cards__card-btns_icon' />
        </button>
        <button
          className='cards__card-btns_delete'
          type='button'
          onClick={() => deleteTask(idTask)}
        >
          <FiTrash2 className='cards__card-btns_icon' />
        </button>
      </div>
    </div>
  );
};
