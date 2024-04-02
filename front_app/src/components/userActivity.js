import React from 'react'
import {useState,useEffect} from 'react'
import {Table} from 'antd';
import { Button, Form, Input, Select, Space } from 'antd';

import Request from '../api';


export const UserActivityList = (props) => {

    const [state, setState]=useState({data:null})

    const columns = [
        {
        title: 'ID',
        dataIndex: 'id',
        key: 'id',
      },
      {
        title: 'Activity',
        dataIndex: 'activity',
        key: 'activity',
        render:(value, row)=> {
            return <span> {value.name} </span>;
        }
      },
      {
        title: 'User',
        dataIndex: 'user',
        key: 'user',
        render:(value, row)=> {
            return <span> {value.name} </span>;
        }

      },
      {
        title: 'Created at',
        dataIndex: 'created_at',
        key: 'created_at',
      },
      {
        title: 'Completed',
        dataIndex: 'completed',
        key: 'completed',
      },
      {
        title: 'Score',
        dataIndex: 'score',
        key: 'score',

      },

    ];

    useEffect(() => {
        Request.get('/user-activity/')
          .then(function (response) {
            setState({data: response.data.results})
          })
          .catch(function (error) {
            console.log(error);
          })
          .finally(function () {
            console.log('finally block');
        });
    },[])

    return (
        <>
        <a href="/" > Activity List </a>
        {state.data && <Table dataSource={state.data} columns={columns} rowKey="id"/> }
        </>
    )
}
