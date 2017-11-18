import React from 'react';
import PropTypes from 'prop-types';
import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import Subheader from 'material-ui/Subheader';
import StarBorder from 'material-ui/svg-icons/toggle/star-border';
// import {Flex, Item} from 'react-flex';
// import 'react-flex/index.css';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import apiUrls from './ApiUrls';
import {loadPost} from '../actions/components/PostAction';
import CommentListEditable from './comment/CommentListEditable';


const tilesData = [
    {
        img: 'images/grid-list/00-52-29-429_640.jpg',
        title: 'Breakfast',
        author: 'jill111',
    },
    {
        img: 'images/grid-list/burger-827309_640.jpg',
        title: 'Tasty burger',
        author: 'pashminu',
    },
    {
        img: 'images/grid-list/camera-813814_640.jpg',
        title: 'Camera',
        author: 'Danson67',
    },
    {
        img: 'images/grid-list/morning-819362_640.jpg',
        title: 'Morning',
        author: 'fancycrave1',
    },
    {
        img: 'images/grid-list/hats-829509_640.jpg',
        title: 'Hats',
        author: 'Hans',
    },
    {
        img: 'images/grid-list/honey-823614_640.jpg',
        title: 'Honey',
        author: 'fancycravel',
    },
    {
        img: 'images/grid-list/vegetables-790022_640.jpg',
        title: 'Vegetables',
        author: 'jill111',
    },
    {
        img: 'images/grid-list/water-plant-821293_640.jpg',
        title: 'Water plant',
        author: 'BkrmadtyaKarki',
    },
];

class NewsFeed extends React.Component {
    static postObjectShape = {
        id: PropTypes.number.isRequired,
        author: PropTypes.number.isRequired,
        author_username: PropTypes.string.isRequired,
        likes: PropTypes.arrayOf(PropTypes.number).isRequired,
        created: PropTypes.string.isRequired,
        updated: PropTypes.string.isRequired,
        likes_count: PropTypes.number.isRequired,
        comments_count: PropTypes.number.isRequired,
        title: PropTypes.string.isRequired,
        title_image: PropTypes.string.isRequired,
    };

    static propTypes = {
        // id: PropTypes.number.isRequired,
        // postObject: PropTypes.object,
        // isLoaded: PropTypes.bool.isRequired,
        // loadPost: PropTypes.func.isRequired,
    };

    componentDidMount() {
        // if (!this.props.postObject) {
        //     const url = apiUrls.postList + String(this.props.id);
        //     console.log('LoadPost', url);
        //     this.props.loadPost(url);
        // }
    }

    styles = {
        root: {
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-around',
        },
        gridList: {
            width: 500,
            height: 450,
            overflowY: 'auto',
        },
    };

    render() {
        // if (this.props.isLoaded) {
        return (

            <div style={this.styles.root}>
                cwvwevewvwe
                <GridList
                    cellHeight={180}
                    style={this.styles.gridList}
                >
                    <Subheader>News</Subheader>
                    {tilesData.map((tile) => (
                        <GridTile
                            key={tile.img}
                            title={tile.title}
                            subtitle={<span>by <b>{tile.author}</b></span>}
                            actionIcon={<IconButton><StarBorder color="white"/></IconButton>}
                        >
                            <img src={tile.img}/>
                        </GridTile>
                    ))}
                </GridList>
            </div>

        );


        // return <div>Nothing</div>;
        // } else {
        //     return <div className="comments-list">Loading...</div>;
        // }
    }
}

const mapStoreToProps = (store, ownProps) => {
    return {};
    // const posts = store.get('posts');
    // console.log('Post', posts);
    // // debugger;
    // if (posts.getIn(['postList', String(ownProps.id)])) {
    //     return {
    //         id: ownProps.id,
    //         postObject: posts.getIn(['postList', String(ownProps.id)]),
    //         isLoaded: true,
    //     };
    // }
    // return {
    //     id: ownProps.id,
    //     isLoaded: false,
    // };
};
//
const mapDispatchToProps = (dispatch) => {
    return {};
    // return bindActionCreators({loadPost}, dispatch);
};
//
export default connect(mapStoreToProps, mapDispatchToProps)(NewsFeed);