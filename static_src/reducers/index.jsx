import {routerReducer} from 'react-router-redux';
import {combineReducers} from 'redux-immutable';
import comments from './components/CommentReducer';
import posts from './components/PostReducer';


export default combineReducers(
    {
        comments,
        posts,

        router: routerReducer
    }
);

