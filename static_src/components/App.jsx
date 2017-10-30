import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import EventList from './event/EventList';
import LikeList from './like/LikeList';
import CommentListEditable from './comment/CommentListEditable';
import Post from './post/Post';

const injectTapEventPlugin = require('react-tap-event-plugin');

injectTapEventPlugin();

class App extends React.Component {

    render() {
        return (
            <div className="app-root">
                <Link to='/post/'>Post</Link>
                <Link to='/'>Home</Link>
                <Switch>
                    <Route exact path="/" component={CommentListEditable}/>
                    <Route exact path="/post/" render={(props) => <Post {...props} id={15}/>}/>
                </Switch>
            </div>
            // <CommentListEditable/>
            // <LikeList/>

            // <EventList/>
        );
    }
}

export default App;