import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import AppBar from 'material-ui/AppBar';


import App from './components/App';
import initStore from './utils/Store';

const AppContent = () => (
    <MuiThemeProvider muiTheme={getMuiTheme(lightBaseTheme)}>
        <AppBar title="My AppBar"/>
        <App/>
    </MuiThemeProvider>
);

ReactDOM.render(
    <Provider store={initStore()}>
        <AppContent/>
    </Provider>,
    document.getElementById('root'),
);