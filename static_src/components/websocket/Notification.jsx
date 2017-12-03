import React from 'react';
import {cent} from 'react-cent';
import Snackbar from 'material-ui/Snackbar';

// Make Centrifuge client accessible through `this.props.cent`
@cent
export class Notification extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            autoHideDuration: 4000,
            message: '',
            open: false,
        };

        // Subscribe on `notification` channel.
        this.props.cent.subscribe('notification', message => {
            console.log(message);
            this.handleMessage(message);
            // }).history().then(history => {
            //     this.handleHistory(history);
        });
    }

    handleHistory(history) {
        console.log('history', history.data);
    }

    handleMessage(message) {
        this.setState({
            message: message.data.message,
            open: true,
        });
    }

    handleActionTouchTap = () => {
        this.setState({
            open: false,
        });
    };

    handleChangeDuration = (event) => {
        const value = event.target.value;
        this.setState({
            autoHideDuration: value.length > 0 ? parseInt(value) : 0,
        });
    };

    render() {
        return (
            <div>
                <Snackbar
                    open={this.state.open}
                    message={this.state.message}
                    action="view"
                    autoHideDuration={this.state.autoHideDuration}
                    onActionTouchTap={this.handleActionTouchTap}
                    onRequestClose={this.handleRequestClose}
                />
            </div>
        );
    }
}