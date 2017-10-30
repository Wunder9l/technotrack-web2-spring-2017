import {CALL_API} from 'redux-api-middleware';
import {normalize} from 'normalizr';
import {post} from '../../utils/Schemas';

export const START_POST_LOADING = 'START_POST_LOADING';
export const SUCCESSFUL_POST_LOADING = 'SUCCESSFUL_POST_LOADING';
export const ERROR_POST_LOADING = 'ERROR_POST_LOADING';


export const loadPost = (url) => {
    return {
        [CALL_API]: {
            credentials: 'include',
            endpoint: url,
            method: 'GET',
            types: [START_POST_LOADING,
                {
                    type: SUCCESSFUL_POST_LOADING,
                    payload: (action, state, res) => {
                        return res;
                        // return getJSON(res).then(
                        //     (json) => {
                        //         console.log('json', json);
                        //         const normalizedData = normalize(json.results, [post]);
                        //         delete json.results;
                        //         return Object.assign({}, json, normalizedData);
                        //     },
                        // );
                    },
                },
                ERROR_POST_LOADING],
        },
    };
};
