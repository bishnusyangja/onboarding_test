import React from 'react';
import './App.css';
import {createBrowserRouter, RouterProvider} from "react-router-dom";

import {UserActivityList} from './components/userActivity';
import {ActivityList, ActivityForm} from './components/activity';


const router = createBrowserRouter([
  {
    path: "/",
    element: <ActivityList/>,
  },
  {
    path: "/user-activity-list",
    element: <UserActivityList/>,
  },
  {
    path: "/activity-create",
    element: <ActivityForm/>,
  },

]);

function App() {
  return <div style={{margin: '50px', padding:'20px'}}><RouterProvider router={router}> </RouterProvider></div>
}

export default App;
