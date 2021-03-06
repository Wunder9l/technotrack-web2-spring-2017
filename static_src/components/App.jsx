import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';

import '../styles/base.scss';
import EventList from './event/EventList';
import LikeList from './like/LikeList';
import CommentListEditable from './comment/CommentListEditable';
import NewsFeed from './NewsFeed';
import Post from './post/Post';

const injectTapEventPlugin = require('react-tap-event-plugin');

injectTapEventPlugin();

class App extends React.Component {

    render() {
        return (
            <div className="wrapper">
                <Link to='/post/'>Post</Link>
                <Link to='/'>Home</Link>
                <header className="header">Header</header>
                <article className="main">
                    <Switch>
                        {/*<Route exact path="/" component={NewsFeed}/>*/}
                        <Route exact path="/" component={CommentListEditable}/>
                        <Route exact path="/post/" render={(props) => <Post {...props} id={15}/>}/>
                    </Switch>
                </article>
                <aside className="aside aside-left">Aside 1</aside>
                <aside className="aside aside-right">Aside 2</aside>
                <footer className="footer">Footer</footer>
            </div>
        );
    }
}

export default App;