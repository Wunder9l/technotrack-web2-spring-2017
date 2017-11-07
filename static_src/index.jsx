import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import AppBar from 'material-ui/AppBar';
import createHistory from 'history/createBrowserHistory';
import {routerMiddleware, ConnectedRouter} from 'react-router-redux';
// import {GridContainer, GridItem} from 'react-css-grid-layout';
import App from './components/App';
import initStore from './utils/Store';

const AppContent = () => (
    <MuiThemeProvider muiTheme={getMuiTheme(lightBaseTheme)}>
        <AppBar title="My AppBar"/>
        <App/>
    </MuiThemeProvider>
);

const history = createHistory();
const middleware = routerMiddleware(history);
ReactDOM.render(
    <Provider store={initStore([middleware])}>
        <ConnectedRouter history={history}>
            <AppContent/>
        </ConnectedRouter>
    </Provider>,
    document.getElementById('root'),
);