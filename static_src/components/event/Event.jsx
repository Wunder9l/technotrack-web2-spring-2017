import React from 'react';
import PropTypes from 'prop-types';

class Event extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        user: PropTypes.shape({
            username: PropTypes.string,
        }).isRequired,
    };
    static defaultProps = {};

    render() {
        return (
            <div className="event-item">
                <div className="event-item-title">
                    Title: {this.props.title}
                </div>
                <div className="event-item-title">
                    User: {this.props.user.username}
                </div>
            </div>
        );
    }
}

export default Event;