# Spotify-Restart-on-Ad [Windows]
This program restarts and triggers the systemwide play-pause button in the event of an advertisement on Spotify.
The aim is to create as close to an Anti-Advert Spotify as possible

This light-weight utility runs in the background silently and invisibly and *does not hamper* <sup>†</sup> your daily workflow.

## How to run
1. Run `Implant and Run.pyw` to "implant" the main file (`spotify restart.pyw`) in the startup directory so that it activates everytime on system boot.
2. Either restart your system now or run `spotify restart.pyw`
3. Enjoy an Anti-Ad experience on non-pro Spotify! (No need to do anything on Spotify, just keep listening as usual)


### Basic Info
**The application makes two short beeps [a high and a low] indicating that it has started and is ready for action all day long!**

Two known bugs still exists, which may possibly crash this anti-ad program or let some specific ads skip through. In case this happens, restart `spotify restart.pyw` and wait for the beeps again.

## Known issue(s)
If Spotify restarts, well and good, if not, then the ad has successfully escaped detection and will continue to do so [Detection of escaping ads may require an entire redesign of this program]. But, for now, the escaping-ads issue can be solved by running the second program `manual spotify restart.pyw`.

## Future plans
1. Restart Spotify in minimized window so as to not block user's workflow at all.
2. Detect EVERY ad (find a way to detect refugee ads).
3. Make sure the systemwide play-pause button is only pressed when the application ***fully loads up*** on restart?

\
\
†The Spotify app restarts in fullscreen/normal size and blocks view temporarily unless minimized again.
