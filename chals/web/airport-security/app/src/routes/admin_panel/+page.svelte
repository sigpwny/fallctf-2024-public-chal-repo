<script lang="ts">
  import { enhance } from "$app/forms";
	import type { ActionData, PageServerData } from "./$types";

  let from_text: string = "";
  export let form: ActionData;
</script>

<div class="bg-gray-200 p-4 font-mono">
  <div class="bg-black text-white p-2 text-xl">Flight Query Panel</div>

  <div class="bg-white p-2 border border-gray-400 mb-4 my-4">
    <pre class="whitespace-pre-wrap">{`SELECT "flight_number", "to", "from" FROM "Flight" WHERE "from" LIKE '${from_text}%' ORDER BY "flight_number" ASC`}</pre>
  </div>

  <form class="my-4" method="post" use:enhance on:submit={() => from_text = ""}>
    <input
      type="text"
      id="from_text"
      name="from_text"
      placeholder="Search Flights by From (Leave empty to see all flights)"
      class="p-2 w-full border border-gray-400 mb-4"
      bind:value={from_text}
    />
    <button class="p-2 bg-gray-400 text-black w-full">Search</button>
  </form>

  {#if form?.error}
    <div class="bg-red-100 text-red-600 p-2 mb-4 border border-red-400">
      {@html form?.message}
    </div>
  {/if}

  <table class="w-full border-collapse border border-gray-400 mt-4">
    <thead>
      <tr class="bg-gray-300">
        <th class="border border-gray-400 p-2">Flight Number (flight_number)</th>
        <th class="border border-gray-400 p-2">To (to)</th>
        <th class="border border-gray-400 p-2">From (from)</th>
        <th class="border border-gray-400 p-2">Details (details)</th>
      </tr>
    </thead>
    <tbody>
      {#if form?.error === false}
        {#each form?.message as flight}
        <tr class="text-center">
          <td class="border border-gray-400 p-2">{flight.flight_number}</td>
          <td class="border border-gray-400 p-2">{flight.to}</td>
          <td class="border border-gray-400 p-2">{flight.from}</td>
          <td class="border border-gray-400 p-2">Details are not implemented in the display yet</td>
        </tr>
        {/each}
      {/if}
      
    </tbody>
  </table>
</div>
