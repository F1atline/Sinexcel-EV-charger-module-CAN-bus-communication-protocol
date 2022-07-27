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
    <tbody>
        <tr>
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

#### **Protocol code**

Value `0x60` indicates the communication protocol number between the DC charging module and the
upper controller.

#### **Destination address**

Used to define the destination address associated with this frame during frame delivery. When
sent from the upper controller, this address is the address of the DC charging module; when sent
from the DC charging module, this address is the controller address (recommended to `0x0f0+N`).

#### **The source address**

<p>Used to define the source address associated with this frame during frame delivery. When sent
from the upper controller, this address is the address of the controller; when sent from the DC
charging module, this address is the address of the module.</p>
DC charging module address (11bits) is defined as follows:
<table>
    <thead>
        <tr>
            <th colspan=5>Group № (5 bit)</th>
            <th colspan=6>Subaddress (6 bit)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
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

Where:

- **Group number** <br>
  When there are multiple modules on the same CAN bus, you can divide them into different groups by setting different group numbers.
  After that, the group module is conveniently controlled by the corresponding group broadcast command (commands that control all modules), and the effective group number is ***0-30***, (***31*** is reserved for global broadcast).
- **Subaddress** <br> 
  The valid range of the subaddress of the module is 1-63. When the specific module is to be
  accurately controlled or read, the group number + subaddress can be used to accurately control the corresponding module or read the corresponding module information.

#### **Group broadcast command and global broadcast command**

<p>When the subaddress is 0, the group number is 0-30, indicating that this command is a group
broadcast command, all the modules in this group will receive relevant data, or receive
corresponding control commands.</p>
<p>When the subaddress is 0, the group number is 31, indicating that this command is a global
broadcast command, all modules on the CAN bus will receive relevant data, or receive corresponding
control commands.</p>

### Data Feild

The Data Field consist of Message type, Error type, Message ID, Message.
<table>
    <thead>
        <tr>
            <th>Message type</th>
            <th>Error type</th>
            <th colspan=2>Message ID</th>
            <th colspan=4>Message</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Byte 0</td>
            <td>Byte 1</td>
            <td>Byte 2</td>
            <td>Byte 3</td> 
            <td>Byte 4</td>
            <td>Byte 5</td>
            <td>Byte 6</td>
            <td>Byte 7</td>
        </tr>
    </tbody>
</table>

#### **Message type**
<table>
    <thead>
        <tr>
            <th>Byte 0</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0x50</td>
            <td>Comprehensive query data command issued by the upper controller</td>
        </tr>
        <tr>
            <td>0x41</td>
            <td>Query information replied by the module</td>
        </tr>
        <tr>
            <td>0x03</td>
            <td>Single setting command issued by the upper controller</td>
        </tr>
        <tr>
            <td>0x43</td>
            <td>Setting information replied by the module</td>
        </tr>
    </tbody>
</table>

#### **Error type**
<table>
    <thead>
        <tr>
            <th>Byte 1</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0xF0</td>
            <td>No error, normal response</td>
        </tr>
        <tr>
            <td>0xF1</td>
            <td>Invalid node address</td>
        </tr>
        <tr>
            <td>0xF2</td>
            <td>Invalid command</td>
        </tr>
        <tr>
            <td>0xF3</td>
            <td>Data verification error</td>
        </tr>
        <tr>
            <td>0xF4</td>
            <td>Address is being identified</td>
        </tr>
    </tbody>
</table>

#### **Message ID**
<table>
    <thead>
        <tr>
            <th>Byte 2</th>
            <th>Byte 3</th>
            <th>Description</th>
            <th>Data type</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0x02</td>
            <td>0x02</td>
            <td>The upper controller batch queries the data of each module. Specifically, the moduleoperating status, fault status, output voltage, output current, and software version.</td>
            <td>Comprehensive</td>
            <td>See the comprehensive query command for details.</td>
        </tr>
        <tr>
            <td>0xFF</td>
            <td>0xFF</td>
            <td>The main module of this group reports the
online information of this group module.</td>
            <td>Bit</td>
            <td>See the monitor module online information for details.</td>
        </tr>
        <tr>
            <td>0xFF</td>
            <td>0xFE</td>
            <td>The main module of this group reports the
online information of this group module.</td>
            <td>Bit</td>
            <td>See the monitor module online information for details.</td>
        </tr>
        <tr>
            <td>0x02</td>
            <td>0x30</td>
            <td>Module On/Off</td>
            <td>Bit</td>
            <td>Each bit of the message content corresponds to the module address (1-31) (1: boot command; 0: shutdown command)</td>
        </tr>
        <tr>
            <td>0x02</td>
            <td>0x32</td>
            <td>Module On/Off</td>
            <td>Bit</td>
            <td>Each bit of the message content corresponds to the module address (32-63) (1: boot command; 0: shutdown command)</td>
        </tr>
        <tr>
            <td>0x02</td>
            <td>0x33</td>
            <td>Set module high or low voltage mode</td>
            <td>Int32</td>
            <td>See module high or low voltage mode settings for details.</td>
        </tr>
        <tr>
            <td>0x00</td>
            <td>0x21</td>
            <td>Set module output voltage</td>
            <td>Int32</td>
            <td>See module output voltage settings for details.</td>
        </tr>
        <tr>
            <td>0x00</td>
            <td>0x22</td>
            <td>Set module output current limit percentage</td>
            <td>Int32</td>
            <td>See module output current limit settings for details.</td>
        </tr>
        <tr>
            <td>0x00</td>
            <td>0x1A</td>
            <td>Modify the module group number online</td>
            <td>Int16</td>
            <td>See the online modification module group number for details.</td>
        </tr>
    </tbody>
</table>

#### **Message Content**
The definition of the message content format depends on the data type definition in Table 1-2.
The upper controller only needs to send a comprehensive query command to query the
comprehensive information of a single module in batches (note that this command cannot be a
broadcast command), as shown in the following table.

<table>
    <thead>
        <tr>
            <th rowspan=2></th>
            <th>Message type</th>
            <th>Error type</th>
            <th colspan=2>Message ID</th>
            <th colspan=4>Message Content</th>
            <th colspan=2>Remarks</th>
        </tr>
        <tr>
            <th>Byte 0</th>
            <th>Byte 1</th>
            <th>Byte 2</th>
            <th>Byte 3</th>
            <th>Byte 4</th>
            <th>Byte 5</th>
            <th>Byte 6</th>
            <th>Byte 7</th>
            <th>Data type</th>
            <th>Unit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The upper controller sends Query command</td>
            <td>0x50</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x02</td>
            <td colspan=4>Fixed to 0</td>
            <td>*</td>
            <td>*</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x02</td>
            <td colspan=2>DC operating status</td>
            <td colspan=2>AC operating</td>
            <td>Int16</td>
            <td>*</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x03</td>
            <td colspan=2>DC Status / Fault 2</td>
            <td colspan=2>DC Status / Fault 1</td>
            <td>bit</td>
            <td>*</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x04</td>
            <td colspan=2>AC Status / Fault 2</td>
            <td colspan=2>AC Status / Fault 1</td>
            <td>bit</td>
            <td>*</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x05</td>
            <td colspan=4>Output voltage (10x magnification)</td>
            <td>Int32</td>
            <td>V</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x06</td>
            <td colspan=4>Output current (100x magnification)</td>
            <td>Int32</td>
            <td>A</td>
        </tr>
        <tr>
            <td>Module reply</td>
            <td>0x41</td>
            <td>0xF0</td>
            <td>0x02</td>
            <td>0x0A</td>
            <td colspan=2>AC version</td>
            <td colspan=2>DC version</td>
            <td>Int16</td>
            <td>*</td>
        </tr>
    </tbody>
</table>