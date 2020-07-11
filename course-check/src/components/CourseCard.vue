<template>
	<div class="course" v-bind:class="assignYear(courseTitleFull)">
		<h3>{{ courseTitleFull }}</h3>
		<hr>
		<p class="description"><strong>Description:</strong> {{ courseDetails }}</p>
		<p><strong>Prerequisites:</strong> {{ coursePrerequisites }}</p>
		<div class="flex-container"><strong>Tags:</strong>
			<span class="tag" v-for="t in tags" v-bind:key="t">{{ t }}
			</span>
		</div>
	</div>
</template>

<script>
export default {
	name: 'CourseCard',
	props: {
		courseTitleFull: String,
		courseDetails: String,
		coursePrerequisites: String,
		tags: Array
	},
	methods: {
		assignYear: function(courseTitleFull){
			var years = {'CCT1':'first', 'CCT2':'second', 'CCT3':'third', 'CCT4':'fourth'};
			var code = courseTitleFull.slice(0, 4);
			return (years[code] ? years[code] : "other");
		}
	}
}
</script>

<style scoped>
.course {
	text-align: left;
	border: 1.5px solid #243649;
	border-radius: 2em;
	padding: 2em;
	margin: 1.5em;
}
.tag {
	border: 1.5px solid #243649;
	border-radius: 2em;
	margin: 0.5em;
	padding: 0.5em;
	background: #F7F9F9;
}
.flex-container {
	display: flex;
	flex-flow: row wrap;
}
hr {
	border: none;
	background: #243649;
	height: 1.5px;
}
.first {
	background: #FFE8BF;
}
.second {
	background: #BADCE8;
}
.third {
	background: #A6D1FF;
}
.fourth {
	background: #CFCCFF;
}
.other {
	background: #FFBFED;
}
</style>
