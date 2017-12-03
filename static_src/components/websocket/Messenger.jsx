import React from 'react';
import {cent} from 'react-cent';

// Make Centrifuge client accessible through `this.props.cent`
@cent
export class Messenger extends React.Component {
    constructor(props) {
        super(props);

        // Subscribe on `messaging` channel.
        this.props.cent.subscribe('messaging', message => {
            console.log(message);
            this.handleMessage(message);
        }).history().then(history => {
            this.handleHistory(history);
        });
    }

    handleMessage(message) {
        console.log('message', message.data);
    }

    handleHistory(history) {
        console.log('history', history.data);
    }

    render() {
        // console.log(this.state);

        return (

            <div className="messenger-dialogue">
            </div>
        );
    }
}