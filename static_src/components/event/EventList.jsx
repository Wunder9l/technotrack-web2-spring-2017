import React from 'react';
import Event from './Event';
import apiUrls from '../ApiUrls';


class EventList extends React.Component {

    state = {eventList: [],};

    componentDidMount() {
        fetch(apiUrls.eventsList, {credentials: 'include'}
        ).then(
            (body) => body.json(),
        ).then(
            (json) => this.setState({eventList: json}),
            // (json) => console.log(json),
        );
    }

    render() {
        const events = this.state.commentList.map(
            item => <Event key={item.id} title={item.title} user={item.user}/>
        );
        // console.log(this.state);

        return (

            <div className="event-list">
                {events}
            </div>
        );
    }
}

export default EventList;