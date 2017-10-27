import {createStore, applyMiddleware, compose} from 'redux';
import reducers from '../reducers';
import middlewares from '../middlewares';


function initStore(additionalMiddlewares = []) {
    const initialStore = {};
    return createStore(
        reducers,
        initialStore,
        compose(applyMiddleware(...additionalMiddlewares, ...middlewares)),
    );
}