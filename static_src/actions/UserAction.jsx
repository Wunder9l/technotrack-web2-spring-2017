import {CALL_API} from 'redux-api-middleware';

export const START_COMMENT_LOADING = 'START_COMMENT_LOADING';
export const SUCCESSFUL_COMMENT_LOADING = 'SUCCESSFUL_COMMENT_LOADING';
export const ERROR_COMMENT_LOADING = 'ERROR_COMMENT_LOADING';
export const ADD_COMMENT = 'ADD_COMMENT';


export const updateUsersListComments = (url) => {
    return {
        [CALL_API]: {
            credentials: 'include',
            endpoint: url,
            method: 'GET',
            types: [START_COMMENT_LOADING, SUCCESSFUL_COMMENT_LOADING, ERROR_COMMENT_LOADING],
        },
    };
};