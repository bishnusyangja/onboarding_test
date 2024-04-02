import React from 'react'
import {useState,useEffect} from 'react'
import {Table} from 'antd';
import { Button, Form, Input, Switch} from 'antd';

import Request from '../api';


export const ActivityList = (props) => {

    const [state, setState]=useState({data:null})
    const columns = [
        {
        title: 'ID',
        dataIndex: 'id',
        key: 'id',
      },
      {
        title: 'Name',
        dataIndex: 'name',
        key: 'name',
      },
      {
        title: 'Description',
        dataIndex: 'description',
        key: 'description',
      },
      {
        title: 'Active',
        dataIndex: 'is_active',
        key: 'is_active',
      },
      {
        title: 'Start Date',
        dataIndex: 'start_date',
        key: 'start_date',
      },
      {
        title: 'End Date',
        dataIndex: 'end_date',
        key: 'end_date',
      },
      {
        title: 'Created at',
        dataIndex: 'created_at',
        key: 'created_at',
      },

    ];

    useEffect(() => {
        Request.get('/activity/')
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
        <a href="/user-activity-list" > User Activity List </a>
        <a href="/activity-create" style={{marginLeft: '30px'}}> Create New Activity </a>
        {state.data && <Table dataSource={state.data} columns={columns} rowKey="id"/> }
        </>
    )
}

export const ActivityForm = (props) => {
    const componentSize = 'default';
    const onFormLayoutChange = () => {
        console.log("Nothing");
    }

    return(
    <>
    <a href="/" >Activity List</a>

    <Form
          labelCol={{
            span: 4,
          }}
          wrapperCol={{
            span: 14,
          }}
          layout="horizontal"
          initialValues={{
            size: componentSize,
          }}
          onValuesChange={onFormLayoutChange}
          size={componentSize}
          style={{
            maxWidth: 600,
          }}
        >
        <Form.Item label="Activity Name">
            <Input />
         </Form.Item>

        <Form.Item label="Description">
            <Input.TextArea />
        </Form.Item>
        <Form.Item label="Active" valuePropName="checked">
            <Switch />
        </Form.Item>

         <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
    </Form>
    </>
    )
}
