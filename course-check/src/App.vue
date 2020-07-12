<template>
  <div id="app">
	<ThePreface/>
	<div>
		<div v-for="year in yearFilters" v-bind:key="year.id">
			<input v-model="year.value" type="checkbox" id="year.id" value="year.id" name="year.id">
			<label for="year.id">{{ year.text }}</label>
		</div>
		
		<div v-for="topic in topicFilters" v-bind:key="topic.id">
			<input v-model="topic.value" type="checkbox" id="topic.id" value="topic.id" name="topic.id">
			<label for="topic.id">{{ topic.id }}</label>
		</div>

		<CourseCard 
			v-for="course in Object.keys(courseData).sort()"
			v-bind:key="courseData[course].courseTitleFull"
			v-bind:courseTitleFull="courseData[course].courseTitleFull"
			v-bind:courseDetails="courseData[course].courseDetails"
			v-bind:coursePrerequisites="courseData[course].coursePrerequisites"
			v-bind:tags="courseData[course].tags"
			v-bind:visible="isFilteredOut(course)"
		/>
	</div>
  </div>
</template>

<script>
import ThePreface from './components/ThePreface.vue'
import CourseCard from './components/CourseCard.vue'
import courseData from './json/course-data.json'

export default {
	name: 'App',
	data(){
		return {
			courseData: courseData,
			yearFilters: [
				{id: "firstYearFilter", text: "1st year", value: false},
				{id: "secondYearFilter", text: "2nd year", value: false},
				{id: "thirdYearFilter", text: "3rd year", value: false},
				{id: "fourthYearFilter", text: "4th year", value: false}
			],
			topicFilters: [
				{id: "Advertising", value: false},
				{id: "Design", value: false},
				{id: "Experiential", value: false},
				{id: "Game", value: false},
				{id: "Human", value: false},
				{id: "Internship", value: false},
				{id: "Management", value: false},
				{id: "Marketing", value: false},
				{id: "Media", value: false},
				{id: "Politics", value: false},
				{id: "Programming", value: false},
				{id: "Research", value: false},
				{id: "Software", value: false}
			]
		}
	},
	components: {
		ThePreface,
		CourseCard
	},
	methods: {
		isFilteredOut: function(course){
			return (this.displayCourses[course]);
		},
		getYear: function(course){
			return parseInt(course.slice(3, 4));
		}
	},
	computed: {
		yearFiltersUsed: function(){
			var total = 0;
			for (var f in this.yearFilters) {
				total += this.yearFilters[f].value ? 1 : 0;
			} return total;
		},
		displayCourses: function(){
			var show = {};
			var year;
			var keys = Object.keys(courseData).sort();
			for (var k in keys){
				year = this.getYear(keys[k])-1;
				show[keys[k]] = this.yearFiltersUsed ==  0 ? true : this.yearFilters[year].value;
			}
			return show;
		}
	}
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	color: #243649;
}
</style>
