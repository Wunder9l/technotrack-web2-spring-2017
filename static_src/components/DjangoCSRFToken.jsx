import React from 'react';

import {csrftoken} from '../constants/djangoToken';

const DjangoCSRFToken = () => {
    return (
        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken}/>
    );
};


export default DjangoCSRFToken;