select sum(new_cases) as total_cases, sum(Cast(new_deaths as int)) as total_deaths, 
sum(cast(new_deaths as int))/sum(new_cases)*100 as DeathPercentage
from covid..CovidDeaths
where continent is not null 
order by 1,2


--2 
-- we are taking these out as they are not included in our previous visualisation 
-- and european union is a part of europe


select Location, SUM(cast(new_deaths as int)) as TotalDeathCount
from Covid..CovidDeaths
where continent is null
and location not in ('World','European Union', 'International')
Group by location
order by TotalDeathCount desc


--3

select Location,population, MAX(total_cases) as HighestInfectionCount,MAX((total_cases/population))*100 as PercentPopulationInfected
from Covid..CovidDeaths

Group by location,population
order by PercentPopulationInfected desc


--4 

select Location,population, date, MAX(total_cases) as HighestInfectionCount,MAX((total_cases/population))*100 as PercentPopulationInfected
from Covid..CovidDeaths

Group by location,population,date
order by PercentPopulationInfected desc