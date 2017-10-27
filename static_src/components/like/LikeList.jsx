import React from 'react';
import Like from './Like';
import apiUrls from '../ApiUrls';


class LikeList extends React.Component {

    state = {likeList: [],};

    componentDidMount() {
        fetch(apiUrls.likeList, {credentials: 'include'}
        ).then(
            (body) => body.json(),
        ).then(
            (json) => this.setState({likeList: json}),
            // (json) => console.log(json),
        );
    }

    render() {
        const likeObjects = this.state.likeList.map(
            item => <Like key={item.id} object={item.object} author={item.author} updated={item.updated}/>
        );
        // console.log(this.state);

        return (

            <div className="event-list">
                {likeObjects}
            </div>
        );
    }
}

export default LikeList;