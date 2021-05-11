import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {useHistory } from "react-router-dom";
// import {getPostsThunk} from '../../store/posts'
import "./Posts.css";

function Posts() {
  const dispatch = useDispatch();
  let posts = useSelector(state=>state?.posts)
  const history = useHistory();
  const [makerId, setMakerId] = useState(0)
  const [makerCurrencyId, setMakerCurrencyId] = useState(0)
  const [quantity, setQuantity] = useState(0)
  const [price, setPrice] = useState(0)
  const [makerDirection, setMakerDirection] = useState('offer')


  let numberOfPosts;
  if (posts) {
    numberOfPosts = Object.entries(posts).length
    posts = Object.entries(posts)
  }
function submitTrade(date, makerDirection, price, quantity, makerId) {
  console.log(date, makerDirection, price, quantity, makerId);
  history.push('/')
}
// bidOrOffer: "offer";
// created_on: "Wed, 05 May 2021 00:00:00 GMT";
// id: 1;
// postedCurrencyId: 1;
// price: 1.54325;
// quantity: 25;
// updated_on: "Wed, 05 May 2021 16:50:33 GMT";
// userId: 1;
// wantedCurrencyId: 2;
//todo create a seperate store for search data so this can be accessed
    return (
      <div>
        <div className="currentRate">
          <h2>I am the current exchange rate Div</h2>
        </div>
        <div className="postContainer">
          {numberOfPosts > 0 ? (
            posts.map((post, id) => {

              let date = new Date(
                post[1].created_on
              ).toLocaleDateString();
              return (
                <div key={id} className="singlePost">
                  <div className="postElement">Posted on {date}</div>
                  <div className="postElement">
                    {post[1].bidOrOffer} is at {post[1].price}
                  </div>
                  <div className="postElement">Quantity: {post[1].quantity}</div>
                  <button className="tradeButton"
                  onClick={()=>{submitTrade(
                    date,
                    post[1].bidOrOffer,
                    post[1].price,
                    post[1].quantity,
                    post[1].userId
                  );}}
                  >Trade</button>
                </div>
              );})
          ) : (
            <div>False</div>
          )}
        </div>
      </div>
    );
}

export default Posts;