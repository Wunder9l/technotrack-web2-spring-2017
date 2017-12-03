import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme';
import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import createHistory from 'history/createBrowserHistory';
import {routerMiddleware, ConnectedRouter} from 'react-router-redux';
import {CentProvider} from 'react-cent';
// import {GridContainer, GridItem} from 'react-css-grid-layout';
import App from './components/App';
import initStore from './utils/Store';
import {muiTheme} from './components/design/theme/MyThemeLight';


const AppContent = () => (
    <MuiThemeProvider muiTheme={muiTheme}>
        {/*{getMuiTheme(lightBaseTheme)}*/}
        <App/>
    </MuiThemeProvider>
);

const data = document.querySelector('#centrifuge').dataset || {};
const centrifugeConfig = {
    url: data.url,
    insecure: true, // disable token auth
    user: data.user,
    timestamp: data.timestamp,
    token: data.token,
}

const history = createHistory();
const middleware = routerMiddleware(history);
ReactDOM.render(
    <CentProvider config={centrifugeConfig}>
        <Provider store={initStore([middleware])}>
            <ConnectedRouter history={history}>
                <AppContent/>
            </ConnectedRouter>
        </Provider>
    </CentProvider>,
    document.getElementById('root'),
);