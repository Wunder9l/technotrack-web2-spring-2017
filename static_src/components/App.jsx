import React from 'react';
import EventList from './event/EventList';
import LikeList from './like/LikeList';
import CommentListEditable from './comment/CommentListEditable';

const injectTapEventPlugin = require('react-tap-event-plugin');

injectTapEventPlugin();

class App extends React.Component {

    render() {
        return (
            <CommentListEditable/>
            // <LikeList/>

            // <EventList/>
        );
    }
}

export default App;