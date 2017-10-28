import { composeWithDevTools } from 'redux-devtools-extension';
import {combineReducers, createStore, applyMiddleware, compose} from 'redux';
import reducers from '../reducers';
import middlewares from '../middlewares';


export default function initStore(additionalMiddlewares = []) {
    const reducer = combineReducers(reducers);
    const initialStore = {};
    return createStore(
        reducer,
        initialStore,
        composeWithDevTools(
            applyMiddleware(...additionalMiddlewares, ...middlewares)
        ),
    );
}