# Sinexcel-EV-charger-module-CAN-bus-communication-protocol
Communication Protocol for interaction between the DC Sinexcel EV charger module over CAN bus interface

## CAN protocol specification

### Introduction

<p>The protocol uses the extended frame mode of CAN bus CAN2.0B-"CAN Specification2.0 Part B". All data items transmit the high order of each byte first, followed by the low order of each byte.</p>
<p>The communication baud rate is 125Kbps.</p>

<table>
    <thead>
        <tr>
            <th>Field</th>
            <th>Description</th>
            <th>Size, bit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>Frame header</td>
            <td>29</td>
        </tr>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>64 (8 Byte)</td>
        </tr>
    </tbody>
</table>

### ID Field

The ID field message format is defined as follows:

<table>
    <thead>
        <tr>
            <th colspan=7>Protocol code (7 bit)</th>
            <th colspan=11>Destination address (11 bit)</th>
            <th colspan=11>Source address (11 bit)</th>
        </tr>
    </thead>
        <tr>
            <!-- <style>
                table,
                th,
                td {
                    padding: 10px;
                    border: 1px solid black;
                    border-collapse: collapse;
                    align: center;
                } -->
            </style>
            <td>28</td>
            <td>27</td>
            <td>26</td>
            <td>25</td>
            <td>24</td>
            <td>23</td>
            <td>22</td>
            <td>21</td>
            <td>20</td>
            <td>19</td>
            <td>18</td>
            <td>17</td>
            <td>16</td>
            <td>15</td>
            <td>14</td>
            <td>13</td>
            <td>12</td>
            <td>11</td>
            <td>10</td>
            <td>9</td>
            <td>8</td>
            <td>7</td>
            <td>6</td>
            <td>5</td>
            <td>4</td>
            <td>3</td>
            <td>2</td>
            <td>1</td>
            <td>0</td>
        </tr>
    </tbody>
</table>