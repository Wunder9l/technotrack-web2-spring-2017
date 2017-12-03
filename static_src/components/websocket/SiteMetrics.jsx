import React from 'react';
import {cent} from 'react-cent';

// Make Centrifuge client accessible through `this.props.cent`
@cent
export class SiteMetrics extends React.Component {
    constructor(props) {
        super(props);

        // Subscribe on `site-metrics` channel.
        this.props.cent.subscribe('site-metrics', message => {
            SiteMetrics.handleMessage(message);
        }).history().then(history => {
            this.handleHistory(history);
        });
    }

    static handleMessage(message) {
        console.log('message', message.data);
    }

    handleHistory(history) {
        console.log('history', history.data);
    }
}