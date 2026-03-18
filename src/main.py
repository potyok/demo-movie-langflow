from sqlmodel import SQLModel, Field, create_engine, Session, select, JSON, Column, Relationship, or_, and_
from pydantic import BaseModel
from typing import List, Optional, Literal, Union
from datetime import datetime, timedelta
from fastmcp import FastMCP


##=================================================
## Data models for the Movie and Screening entities

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(description="The title of the movie")
    short_description: str = Field(description="The short description of the movie")
    genre: List[Literal['thriller', 'action', 'adventure', 'drama', 'sci-fi', 'romantic', 'comedy']] = Field(description="The genre the film", sa_column=Column(JSON))
    length: int = Field(description="The length of the movie in minutes")

    screenings: List["MovieScreening"] = Relationship(back_populates="movie")

class MovieScreening(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_id: int = Field(description="The id of the movie", foreign_key="movie.id")
    start_time: datetime = Field(description="The start time of the screening")

    movie: Optional[Movie] = Relationship(back_populates="screenings")

class MovieInfo(BaseModel):
    id: int = Field(description="The id of the movie")
    title: str = Field(description="The title of the movie")

class DetailedMovieInfo(MovieInfo):
    short_description: str = Field(description="The short description of the movie")
    genre: List[Literal['thriller', 'action', 'adventure', 'drama', 'sci-fi', 'romantic', 'comedy']]
    length: int = Field(description="The length of the movie in minutes")
    screenings: List[datetime] = Field(description="The start time of screenings")

##==================================================
## Dabase setup logic and data for inicialization

def setup_db():
    movie_sqlite_url = "sqlite:///movie.db"
    movie_engine = create_engine(movie_sqlite_url)
    SQLModel.metadata.create_all(movie_engine)
    return movie_engine

def init_dummy_data(engine):
    with Session(engine) as session:
        example_movies = [
            Movie(
                title="Interstellar",
                short_description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                genre=["sci-fi", "adventure"],
                length=169,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 20, 9, 0)),  
                    MovieScreening(start_time=datetime(2026, 1, 22, 18, 30)),
                    MovieScreening(start_time=datetime(2026, 1, 25, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 29, 8, 0)),  
                    MovieScreening(start_time=datetime(2026, 2, 2, 10, 0)),  
                    MovieScreening(start_time=datetime(2026, 2, 10, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 15, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 1, 16, 0))
                ]
            ),
            Movie(
                title="The Dark Knight",
                short_description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham.",
                genre=["action", "thriller"],
                length=152,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 21, 10, 0)), 
                    MovieScreening(start_time=datetime(2026, 1, 24, 21, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 28, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 5, 11, 0)),  
                    MovieScreening(start_time=datetime(2026, 2, 12, 16, 0)), 
                    MovieScreening(start_time=datetime(2026, 2, 18, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 5, 14, 0)),   
                    MovieScreening(start_time=datetime(2026, 3, 12, 20, 0))
                ]
            ),
            Movie(
                title="Superbad",
                short_description="Two co-dependent high school seniors are forced to deal with separation anxiety.",
                genre=["comedy"],
                length=113,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 23, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 27, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 1, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 9, 12, 30)), 
                    MovieScreening(start_time=datetime(2026, 2, 14, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 22, 17, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 3, 21, 0))
                ]
            ),
            Movie(
                title="Inception",
                short_description="A thief who steals corporate secrets through the use of dream-sharing technology.",
                genre=["sci-fi", "action"],
                length=148,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 26, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 31, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 6, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 17, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 24, 9, 0)), 
                    MovieScreening(start_time=datetime(2026, 3, 6, 22, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 11, 10, 0)) 
                ]
            ),
            Movie(
                title="Parasite",
                short_description="Greed and class discrimination threaten the newly formed symbiotic relationship.",
                genre=["thriller", "drama"],
                length=132,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 20, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 24, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 3, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 11, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 20, 10, 30)),
                    MovieScreening(start_time=datetime(2026, 3, 2, 11, 0)), 
                    MovieScreening(start_time=datetime(2026, 3, 10, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 15, 11, 0)) 
                ]
            ),
            Movie(
                title="La La Land",
                short_description="While navigating their careers in Los Angeles, a pianist and an actress fall in love.",
                genre=["romantic", "drama"],
                length=128,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 22, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 28, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 7, 21, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 14, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 21, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 28, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 9, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 14, 16, 0))
                ]
            ),
            Movie(
                title="The Grand Budapest Hotel",
                short_description="A writer encounters the owner of a high-class hotel, who tells him of his early years.",
                genre=["comedy", "adventure"],
                length=99,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 21, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 25, 11, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 30, 17, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 8, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 15, 10, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 23, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 4, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 13, 16, 0))
                ]
            ),
            Movie(
                title="Mad Max: Fury Road",
                short_description="In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler.",
                genre=["action", "adventure"],
                length=120,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 23, 10, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 29, 21, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 4, 17, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 12, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 19, 22, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 27, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 8, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 14, 21, 0))
                ]
            ),
            Movie(
                title="Dune",
                short_description="A noble family becomes embroiled in a war for control over the galaxy's most valuable asset.",
                genre=["sci-fi", "adventure"],
                length=155,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 24, 10, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 31, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 10, 15, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 18, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 25, 17, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 7, 21, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 15, 9, 0))
                ]
            ),
            Movie(
                title="Shutter Island",
                short_description="A U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital.",
                genre=["thriller", "drama"],
                length=138,
                screenings=[
                    MovieScreening(start_time=datetime(2026, 1, 20, 22, 0)),
                    MovieScreening(start_time=datetime(2026, 1, 27, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 2, 18, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 11, 21, 0)),
                    MovieScreening(start_time=datetime(2026, 2, 21, 20, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 1, 14, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 8, 19, 0)),
                    MovieScreening(start_time=datetime(2026, 3, 12, 17, 0))
                ]
            )
        ]
        session.add_all(example_movies)
        session.commit()


##==================================================
## Define MCP server and tools

movie_mcp_server = FastMCP('Movie')
movie_engine = setup_db()

@movie_mcp_server.tool()
def get_title_of_movies():
  with Session(movie_engine) as session:
    statement = select(Movie.title)
    results = session.exec(statement).all()
    return results
  
@movie_mcp_server.tool()
def get_screenings_for_movie(movie_title: str):
  with Session(movie_engine) as session:
    statement = select(Movie).where(Movie.title == movie_title)
    result = session.exec(statement).first()
    return result.screenings
  
@movie_mcp_server.tool()
def get_movie_info(movie_id: str) -> DetailedMovieInfo:
    with Session(movie_engine) as session:
        statement = select(Movie).where(Movie.id == movie_id)
        result = session.exec(statement).first()
        return DetailedMovieInfo(
          title=result.title,
          id=result.id,
          short_description=result.short_description,
          genre=result.genre,
          length=result.length,
          screenings=[screening.start_time for screening in result.screenings]
      )

@movie_mcp_server.tool()
def get_movie_info_by_title(movie_title: str) ->DetailedMovieInfo:
   with Session(movie_engine) as session:
        statement = select(Movie).where(Movie.title == movie_title)
        result = session.exec(statement).first()
        return DetailedMovieInfo(
          title=result.title,
          id=result.id,
          short_description=result.short_description,
          genre=result.genre,
          length=result.length,
          screenings=[screening.start_time for screening in result.screenings]
      )
    
@movie_mcp_server.tool()
def search_movies_by_filter(
    genres: Optional[List[Literal['thriller', 'action', 'adventure', 'drama', 'sci-fi', 'romantic', 'comedy']]] = None,
    target_date: Optional[datetime] = None,
    response_format: Literal['concise', 'detailed'] = "detailed"
    ) -> Union[List[MovieInfo], List[DetailedMovieInfo]]:
  with Session(movie_engine) as session:
    statement = select(Movie)

    if target_date:
      start_of_day = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
      end_of_day = start_of_day + timedelta(days=1)
      statement = statement.where(
          Movie.screenings.any(
              and_(
                    MovieScreening.start_time >= start_of_day,
                    MovieScreening.start_time < end_of_day
                )
            )
      )

    if genres:
      conditions = [Movie.genre.contains(g) for g in genres]
      statement = statement.where(or_(*conditions))

    results = session.exec(statement).all()

    if response_format == "concise":
      return [MovieInfo(title=movie.title, id=movie.id) for movie in results]

    return [DetailedMovieInfo(
        title=movie.title,
        id=movie.id,
        short_description=movie.short_description,
        genre=movie.genre,
        length=movie.length,
        screenings=[screening.start_time for screening in movie.screenings if target_date is None or start_of_day <= screening.start_time < end_of_day]
    ) for movie in results]
  

if __name__ == '__main__':
    from pathlib import Path

    db_path = Path("movie.db")
    if not db_path.is_file(): init_dummy_data(movie_engine)
    movie_mcp_server.run(transport='streamable-http')