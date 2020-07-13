<template>
	<div class="filterGroup">
		<label><strong>{{ filterTitle }}</strong></label><br><br>
		<div v-for="filter in filterOptions" v-bind:key="filter.id" class="filter">
			<input v-model="filter.value" type="checkbox" v-bind:id="filter.id" v-bind:value="filter.id" v-bind:name="filterGroupName">
			<label v-bind:for="filter.id">{{ filter.text }}</label>
		</div>
	</div>
</template>

<script>
export default {
	name: 'CourseFilter',
	props: {
		filterGroupName: String,
		filterTitle: String,
		filterOptions: Array
	}
}
</script>

<style scoped>
.filter {
	margin: 0.5em 0 0 0;
}
.filterGroup {
	margin-bottom: 1em;
	padding: 1.5em;
	border: 1.5px solid #243649;
	border-radius: 2em;
	background: #E6E8E8;
}
</style>
