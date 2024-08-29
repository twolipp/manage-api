import React from "react";
import { gql, useQuery } from "@apollo/client";

const QUERY = gql`
  query {
    programmer(programmerId: 1) {
      name
    }
  }
`;

const HomePage = () => {
  const { data, loading, error } = useQuery(QUERY);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    console.error(error);
    return null;
  }

  return (
    <div>
      <h1>An Awesome Template </h1>
      <h3>On Django, Next, Postgres, and Docker </h3>
      <p>{data.programmer.name}</p>
    
    </div>
  );
};

export default HomePage;
