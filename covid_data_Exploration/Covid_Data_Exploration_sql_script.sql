Select * 
From Covid..CovidDeaths
where continent is not null
order by 3,4


--Select * 
--From Covid..CovidVaccination
--order by 3,4

--Select Data that we are going to be using 
Select Location, date, total_cases, new_cases,total_deaths,population
from Covid..CovidDeaths
order by 1,2


-- looking at the total cases vs total deaths 
-- shows likelihood of dying if you contact in your country
Select Location, date, total_cases, total_deaths,(total_deaths/total_cases)*100 as Deathpercentage
from Covid..CovidDeaths
Where location like '%India%'
order by 1,2


-- Looking at total cases vs population
--shows what percentage of population got covid

Select Location, date, total_cases, Population, (total_cases/population)*100 as percentageofgettingcovid
from Covid..CovidDeaths
Where location like '%India%'
order by 1,2


--looking at countries with highest infection rate compared to population
Select Location, MAX(total_cases) as highestinfectioncount, Population, Max((total_cases/population))*100 as percentageofgettingcovid
from Covid..CovidDeaths

Group by location,population
order by percentageofgettingcovid desc

-- showing countries with highest death count per population

Select Location, MAX(cast(total_deaths as int)) as highestdeathscount
from Covid..CovidDeaths

where continent is not null
Group by location
order by highestdeathscount desc

-- looking acc. to continent
Select continent, MAX(cast(total_deaths as int)) as highestdeathscount
from Covid..CovidDeaths

where continent is  not null
Group by continent
order by highestdeathscount desc


-- showing continent with highes deat count per population
Select continent, MAX(cast(total_deaths as int)) as highestdeathscount
from Covid..CovidDeaths
where continent is  not null
Group by continent
order by highestdeathscount desc


-- global numbers
Select  SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as Deathpercentage
from Covid..CovidDeaths

where continent is not null
--Group by date
order by 1,2




-- looking population vs total vaccination
Select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
SUM(convert(int,vac.new_vaccinations )) Over (Partition by dea.location order by dea.location, dea.date) as total_vac

from Covid..CovidDeaths as dea
join covid..CovidVaccination as vac
	on dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
order by 2,3


-- use cte
with VacacPop(Continent,Location, Date, Population,new_vaccinations, total_vac)
as
(
Select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
SUM(convert(int,vac.new_vaccinations )) Over (Partition by dea.location order by dea.location, dea.date) as total_vac

from Covid..CovidDeaths as dea
join covid..CovidVaccination as vac
	on dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3
)

select *, (total_vac/population)*100
from VacacPop


-- Temp Table
Drop Table if exists #PercentPopulationVaccinated  -- only if you are making any alterations in the existing table then you can use it 
create table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
total_vac numeric
)


Insert Into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
SUM(convert(int,vac.new_vaccinations )) Over (Partition by dea.location order by dea.location, dea.date) as total_vac

from Covid..CovidDeaths as dea
join covid..CovidVaccination as vac
	on dea.location = vac.location
	and dea.date = vac.date
--where dea.continent is not null
--order by 2,3

select *, (total_vac/population)*100 as total_vac_VS_pop
from #PercentPopulationVaccinated



--creating view to store data for later visualizations 
Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
SUM(convert(int,vac.new_vaccinations )) Over (Partition by dea.location order by dea.location, dea.date) as total_vac

from Covid..CovidDeaths as dea
join covid..CovidVaccination as vac
	on dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3


select *
from PercentPopulationVaccinated



