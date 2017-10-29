import {composeWithDevTools} from 'redux-devtools-extension';
import {fromJS, Map} from 'immutable';
import {createStore, applyMiddleware} from 'redux';
import reducers from '../reducers';
import middlewares from '../middlewares';


export default function initStore(additionalMiddlewares = []) {
    const initialStore = Map({
        comments: {
            commentList: [],
            isLoading: false,
        },
    });
    console.log("INIT:", typeof (initialStore));
    return createStore(
        reducers,
        initialStore,
        composeWithDevTools(
            applyMiddleware(...additionalMiddlewares, ...middlewares),
        ),
    );
}