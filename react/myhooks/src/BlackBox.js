import React, { useState } from 'react';

export default function BlackBox(props) {
  const [count, setCount] = useState(0);

  const getCount = () => {
    return count;
  };
  
  return (
    <div>
      {props.boxName}
    </div>
  );
}
